use r2r::QosProfile;
use tokio::task;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let ctx = r2r::Context::create()?;
    let mut node = r2r::Node::create(ctx, "testnode", "")?;
    let duration = std::time::Duration::from_millis(2500);

    let mut timer = node.create_wall_timer(duration)?;
    let publisher =
        node.create_publisher::<r2r::std_msgs::msg::String>("/hw_topic", QosProfile::default())?;

    task::spawn(async move {
        loop {
            timer.tick().await.unwrap();
            let msg = r2r::std_msgs::msg::String {
                data: "hello world".to_string(),
            };
            publisher.publish(&msg).unwrap();
            std::thread::sleep(std::time::Duration::from_millis(100));
        }
    }); 

    // here we spin the node in its own thread (but we could just busy wait in this thread)
    let handle = std::thread::spawn(move || loop {
        node.spin_once(std::time::Duration::from_millis(100));
    });
    handle.join().unwrap();

    Ok(())
}