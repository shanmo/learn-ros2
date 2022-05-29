use std::sync::Arc;

use rclrust::{qos::QoSProfile, rclrust_info};
use rclrust_msg::std_msgs::msg::String as String_;
use rclrust_msg::std_msgs::msg::UInt8 as u8_;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let ctx = rclrust::init()?;
    let mut node = ctx.create_node("billy_reader")?;
    let logger = node.logger();
    let publisher = node.create_publisher::<u8_>("reward", &QoSProfile::default())?;
    let reward: u8 = 10; 

    let _subscription = node.create_subscription(
        "blog",
        move |msg: Arc<String_>| {
            rclrust_info!(logger, "I read: {}", msg.data);
            publisher.publish(&u8_ {
                data: reward,
            }).unwrap();
            rclrust_info!(logger, "I paid: ${} for the blog", reward);
        },
        &QoSProfile::default(),
    )?;

    node.wait();
    Ok(())
}

