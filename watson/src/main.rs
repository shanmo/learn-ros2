use std::{thread::sleep, time::Duration};
use std::sync::Arc;

use anyhow::Result;
use rclrust::{qos::QoSProfile, rclrust_info};
use rclrust_msg::std_msgs::msg::String as String_;
use rclrust_msg::std_msgs::msg::UInt8 as u8_;

#[tokio::main]
async fn main() -> Result<()> {
    let ctx = rclrust::init()?;
    let mut node = ctx.create_node("watson_blog")?;
    let logger = node.logger();
    let publisher = node.create_publisher::<String_>("blog", &QoSProfile::default())?;

    let _subscription = node.create_subscription(
        "reward",
        move |msg: Arc<u8_>| {
            rclrust_info!(logger, "I received ${} reward", msg.data);
        },
        &QoSProfile::default(),
    )?;

    let logger = node.logger();
    let mut count = 1; 
    loop {
        publisher.publish(&String_ {
            data: format!("Watson's {}th blog", count),
        })?;
        rclrust_info!(logger, "Watson's {}th blog published", count);
        count += 1; 
        sleep(Duration::from_millis(100));
    }

    Ok(())
}