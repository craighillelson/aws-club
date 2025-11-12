from ipaddress import ip_network
import random

def generate_random_private_network(range_choice=None):
    """Generate a random private IP network with proper alignment"""
    if range_choice is None:
        range_choice = random.choice(['10', '172', '192'])
    
    if range_choice == '10':
        # 10.0.0.0/8 range
        prefix = random.choice([16, 20, 24])
        
        if prefix == 16:
            octet2 = random.randint(0, 255)
            return f"10.{octet2}.0.0/16"
        elif prefix == 20:
            octet2 = random.randint(0, 255)
            octet3 = random.choice([0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240])
            return f"10.{octet2}.{octet3}.0/20"
        else:  # 24
            octet2 = random.randint(0, 255)
            octet3 = random.randint(0, 255)
            return f"10.{octet2}.{octet3}.0/24"
    
    elif range_choice == '172':
        # 172.16.0.0/12 range
        prefix = random.choice([16, 20, 24])
        
        if prefix == 16:
            octet2 = random.randint(16, 31)
            return f"172.{octet2}.0.0/16"
        elif prefix == 20:
            octet2 = random.randint(16, 31)
            octet3 = random.choice([0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240])
            return f"172.{octet2}.{octet3}.0/20"
        else:  # 24
            octet2 = random.randint(16, 31)
            octet3 = random.randint(0, 255)
            return f"172.{octet2}.{octet3}.0/24"
    
    else:  # 192
        # 192.168.0.0/16 range
        prefix = random.choice([20, 24])
        
        if prefix == 20:
            octet3 = random.choice([0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240])
            return f"192.168.{octet3}.0/20"
        else:  # 24
            octet3 = random.randint(0, 255)
            return f"192.168.{octet3}.0/24"

def test_networks_random():
    """Quiz mode: User determines if randomly generated networks overlap"""
    # Choose a single class for both networks
    range_choice = random.choice(['10', '172', '192'])
    
    # Generate both networks in the same class
    network1_input = generate_random_private_network(range_choice)
    network2_input = generate_random_private_network(range_choice)
    
    print(f"\nNetwork 1: {network1_input}")
    print(f"Network 2: {network2_input}")
    
    # Get user's prediction
    user_answer = input("\nDo these networks overlap? (yes/no): ").lower()
    
    try:
        net1 = ip_network(network1_input)
        net2 = ip_network(network2_input)
        
        # Check actual overlap
        actual_overlap = net1.overlaps(net2)
        user_thinks_overlap = user_answer in ['yes', 'y']
        
        # Validate user's answer
        print("\n" + "="*50)
        if user_thinks_overlap == actual_overlap:
            print("✅ CORRECT!")
        else:
            print("❌ INCORRECT!")
        
        # Show the actual result
        if actual_overlap:
            print(f"\nThese networks DO overlap - CONFLICT")
            if net1.subnet_of(net2):
                print(f"  └─ {net1} is a subnet of {net2}")
            elif net2.subnet_of(net1):
                print(f"  └─ {net2} is a subnet of {net1}")
        else:
            print(f"\nThese networks do NOT overlap - Okay")
        
        print("="*50)
            
    except ValueError as e:
        print(f"Error: {e}")

def test_networks_manual():
    """Test user-provided networks"""
    network1_input = input("Enter first network (e.g., 10.0.1.0/24): ")
    network2_input = input("Enter second network (e.g., 10.0.1.128/25): ")
    
    try:
        net1 = ip_network(network1_input)
        net2 = ip_network(network2_input)
        
        print(f"\nNetwork 1: {net1}")
        print(f"Network 2: {net2}")
        
        # Visual overlap indicator
        if net1.overlaps(net2):
            print(f"\n❌ CONFLICT - Networks overlap!")
        else:
            print(f"\n✅ Okay - No overlap")
        
        # Bonus: Check if one is a subnet of the other
        if net1.subnet_of(net2):
            print(f"  └─ {net1} is a subnet of {net2}")
        elif net2.subnet_of(net1):
            print(f"  └─ {net2} is a subnet of {net1}")
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Make sure you use CIDR notation (e.g., 10.0.0.0/16)")

def show_menu():
    """Display menu and get user choice"""
    print("\n=== Network Overlap Checker ===")
    print("1. Quiz mode - Test your knowledge with random networks")
    print("2. Check mode - Enter your own networks to test")
    print("3. Exit")
    choice = input("\nChoose an option (1-3): ")
    return choice

# Main loop
while True:
    choice = show_menu()
    
    if choice == '1':
        print("\n" + "-"*50)
        test_networks_random()
    elif choice == '2':
        print("\n" + "-"*50)
        test_networks_manual()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")
    
    input("\nPress Enter to continue...")
