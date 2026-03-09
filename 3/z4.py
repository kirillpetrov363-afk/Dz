class VideoCard:

    manufacturer: str = "Unknown"
    category: str = "GPU"

    def __init__(self, brand: str, model: str, memory: int, year: int, price: int) -> None:
        self.brand = brand
        self.model = model
        self.memory = memory
        self.year = year
        self.price = price

    def __str__(self) -> str:
        return f"{self.brand} {self.model}, {self.memory}GB ({self.year})"

    def is_powerful(self) -> bool:
        return self.memory >= 8

    def change_price(self, new_price: int) -> None:
        self.price = new_price

    def get_age(self, current_year: int) -> int:
        return current_year - self.year

    def change_manufacturer(self, new_manufacturer: str) -> None:
        VideoCard.manufacturer = new_manufacturer


gpu1 = VideoCard("NVIDIA", "RTX 3060", 12, 2021, 350)
gpu2 = VideoCard("AMD", "RX 6600", 8, 2021, 300)
gpu3 = VideoCard("NVIDIA", "RTX 4090", 24, 2022, 1600)


print(gpu1)
print(gpu2.get_age(2025))
print(gpu3.is_powerful())

gpu1.change_price(330)
print(gpu1.price)

gpu2.change_manufacturer("NVIDIA/AMD")
print(VideoCard.manufacturer)