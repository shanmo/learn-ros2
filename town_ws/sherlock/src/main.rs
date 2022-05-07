use futures::executor::LocalPool;
use futures::stream::StreamExt;
use futures::task::LocalSpawnExt;
use r2r::QosProfile;
use futures::future;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let ctx = r2r::Context::create()?;
    let mut node = r2r::Node::create(ctx, "sherlock", "")?;
    let sub = node.subscribe::<r2r::std_msgs::msg::String>("/blog_feedback", QosProfile::default())?;
    let p = node.create_publisher::<r2r::std_msgs::msg::String>("/clue", QosProfile::default())?;
    println!("I am sherlock, elementary my dear watson");

    let mut pool = LocalPool::new();
    let spawner = pool.spawner();

    spawner.spawn_local(async move {
        sub.for_each(|msg| {
            let my_str = "sherlock: new msg from BSI ".to_string() + &msg.data; 
            p.publish(&r2r::std_msgs::msg::String {
                data: my_str.clone(),
            })
            .unwrap();
            println!("{}", my_str);
            future::ready(())
        })
        .await
    })?;

    loop {
        node.spin_once(std::time::Duration::from_millis(100));
        pool.run_until_stalled();
    }
}