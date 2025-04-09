class Smartphone:
    def __init__(self, brand, model, screen_size, battery_capacity):
        self.brand = brand
        self.model = model
        self.screen_size = screen_size
        self.battery_capacity = battery_capacity
        self.is_powered_on = False
    
    def power_toggle(self):
        self.is_powered_on = not self.is_powered_on
        return f"{self.brand} {self.model} is {'on' if self.is_powered_on else 'off'}"
    
    def get_specs(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nScreen: {self.screen_size} inches\nBattery: {self.battery_capacity}mAh"

class AndroidPhone(Smartphone):
    def __init__(self, brand, model, screen_size, battery_capacity, android_version):
        super().__init__(brand, model, screen_size, battery_capacity)
        self.android_version = android_version
        self.apps = []
    
    def install_app(self, app_name):
        self.apps.append(app_name)
        return f"{app_name} installed successfully on {self.model}"
    
    def get_specs(self):  # Method overriding
        return f"{super().get_specs()}\nAndroid Version: {self.android_version}"

class iPhone(Smartphone):
    def __init__(self, model, screen_size, battery_capacity, ios_version):
        super().__init__("Apple", model, screen_size, battery_capacity)
        self.ios_version = ios_version
    
    def get_specs(self):  # Method overriding
        return f"{super().get_specs()}\niOS Version: {self.ios_version}"

# Example usage
if __name__ == "__main__":
    # Create an Android phone
    samsung = AndroidPhone("Samsung", "Galaxy S23", 6.1, 3900, "Android 13")
    print(samsung.get_specs())
    print(samsung.power_toggle())
    print(samsung.install_app("Instagram"))
    
    print("\n" + "="*30 + "\n")
    
    # Create an iPhone
    iphone = iPhone("iPhone 14", 6.1, 3279, "iOS 16")
    print(iphone.get_specs())
    print(iphone.power_toggle())