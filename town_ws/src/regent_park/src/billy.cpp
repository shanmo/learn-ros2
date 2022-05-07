#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv) {
    rclcpp::init(argc, argv); 
    auto node = std::make_shared<rclcpp::Node>("billy"); 
    RCLCPP_INFO(node->get_logger(), "hi, I am BSI Billy"); 
    rclcpp::spin(node); 
    rclcpp::shutdown(); 
    return 0; 
}