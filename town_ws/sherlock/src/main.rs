use futures::executor::LocalPool;
use futures::stream::StreamExt;
use futures::task::LocalSpawnExt;
use r2r::QosProfile;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let ctx = r2r::Context::create()?;
    let mut node = r2r::Node::create(ctx, "sherlock_node", "")?;
    let mut sub = node.subscribe::<r2r::std_msgs::msg::String>("/billy", QosProfile::default())?;
    let p =
        node.create_publisher::<r2r::std_msgs::msg::String>("/sherlock", QosProfile::default())?;

    let mut pool = LocalPool::new();
    let spawner = pool.spawner();

    spawner.spawn_local(async move {
        loop {
            match sub.next().await {
                Some(msg) => {
                    p.publish(&r2r::std_msgs::msg::String {
                        data: format!("sherlock: new msg: {}", msg.data),
                    })
                    .unwrap();
                }
                None => break,
            }
        }
    })?;

    loop {
        node.spin_once(std::time::Duration::from_millis(100));
        pool.run_until_stalled();
    }
}