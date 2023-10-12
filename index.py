from clothing import Sweater, Shorts

sweater = Sweater("Winter Sweater", "Red", 59.99, "Wool", "ABC123")
shorts = Shorts("Swim Trunks", "Blue & White Paisley", 79.99, "Silk", "556227")

print(sweater)
print(shorts)
shorts.appropriate_seasons
sweater.available_sizes
sweater.sale(20.25)
shorts.sale(95)
