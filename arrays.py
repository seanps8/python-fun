#!/usr/bin/python

def main():
    cities = ['DC', 'Seattle', 'San Diego', 'Baltimore', 'Philly']

    for city in cities:
        if city == 'DC':
            print("Go Nats!")
        elif city == 'Baltimore':
            print("Go Orioles!")

    # Add some to dictionary
    dict = {}
    # Append every other city to dictionary
    for city in cities[::2]:
        dict.append(city)


if __name__ == '__main__':
    main()