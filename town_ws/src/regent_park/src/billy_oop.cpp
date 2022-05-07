#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "std_msgs/msg/u_int32.hpp"

using std::placeholders::_1; 
using std::placeholders::_2; 

class NewsboyNode : public rclcpp::Node {
public:
    NewsboyNode(std::string name) : Node(name) {
        RCLCPP_INFO(this->get_logger(), "hi, I am %s", name.c_str()); 

        sub_blog = this->create_subscription<std_msgs::msg::String>("blog", 10, std::bind(&NewsboyNode::topic_callback, this, _1));  
        pub_money = this->create_publisher<std_msgs::msg::UInt32>("blog_money", 10); 
        pub_str = this->create_publisher<std_msgs::msg::String>("blog_feedback", 10);
    }
private: 
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_blog;
    rclcpp::Publisher<std_msgs::msg::UInt32>::SharedPtr pub_money; 
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr pub_str;

    void topic_callback(const std_msgs::msg::String::SharedPtr msg) {
        std_msgs::msg::UInt32 money; 
        money.data = 10; 
        pub_money->publish(money);

        std_msgs::msg::String str; 
        str.data = "I have a message for sherlock!"; 
        pub_str->publish(str);  

        RCLCPP_INFO(this->get_logger(), "billy reads: '%s', and pays: %d pound", msg->data.c_str(), money.data); 
    }
}; 

int main(int argc, char **argv) {
    rclcpp::init(argc, argv); 
    auto node = std::make_shared<NewsboyNode>("billy"); 
    rclcpp::spin(node); 
    rclcpp::shutdown(); 
    return 0; 
}