"""
Data Generator for Search Assignment
Generates four datasets with different characteristics for search algorithm analysis.
"""

import random
import json
import os

def generate_datasets():
    """Generate four datasets representing different search scenarios."""

    # Create datasets directory
    if not os.path.exists("datasets"):
        os.makedirs("datasets")

    print("Generating search datasets...\n")

    # ========================================================================
    # Dataset A: Unsorted Customer IDs (100,000 entries)
    # Scenario: Customer lookup system, data arrives in order received
    # ========================================================================
    print("Dataset A: Unsorted Customer IDs")
    print("  Scenario: Customer service database")
    print("  Size: 100,000 entries")
    print("  Characteristics: Unsorted, large volume")

    customer_ids = list(range(1000000, 1100000))
    random.shuffle(customer_ids)

    with open("datasets/customer_ids.json", "w") as f:
        json.dump(customer_ids, f)

    print("  ✓ Generated: datasets/customer_ids.json\n")

    # ========================================================================
    # Dataset B: Pre-sorted Product Catalog (50,000 entries)
    # Scenario: E-commerce product search, maintained in sorted order
    # ========================================================================
    print("Dataset B: Pre-sorted Product Catalog")
    print("  Scenario: E-commerce inventory system")
    print("  Size: 50,000 entries")
    print("  Characteristics: Already sorted, optimized for lookup")

    product_ids = sorted([f"PROD{str(i).zfill(6)}" for i in range(50000)])

    with open("datasets/product_catalog.json", "w") as f:
        json.dump(product_ids, f)

    print("  ✓ Generated: datasets/product_catalog.json\n")

    # ========================================================================
    # Dataset C: Small Config Settings (500 entries)
    # Scenario: Application configuration lookup
    # ========================================================================
    print("Dataset C: Small Config Settings")
    print("  Scenario: Application settings lookup")
    print("  Size: 500 entries")
    print("  Characteristics: Small, frequently accessed")

    config_keys = [f"config.setting.{i:03d}" for i in range(500)]
    random.shuffle(config_keys)

    with open("datasets/config_settings.json", "w") as f:
        json.dump(config_keys, f)

    print("  ✓ Generated: datasets/config_settings.json\n")

    # ========================================================================
    # Dataset D: Dictionary Words for Autocomplete (10,000 entries)
    # Scenario: Search-as-you-type feature
    # ========================================================================
    print("Dataset D: Dictionary Words")
    print("  Scenario: Autocomplete/search-as-you-type")
    print("  Size: 10,000 entries")
    print("  Characteristics: Pre-sorted for fast prefix matching")

    # Generate realistic-looking words
    prefixes = ["app", "data", "user", "sys", "log", "auth", "file", "net", "cache", "queue"]
    suffixes = ["handler", "manager", "service", "provider", "controller", "processor", "validator", "factory"]

    words = []
    for i in range(10000):
        if i < 5000:
            word = random.choice(prefixes) + random.choice(suffixes) + str(i)
        else:
            word = f"word{str(i).zfill(5)}"
        words.append(word)

    words = sorted(set(words))[:10000]  # Ensure exactly 10,000 unique sorted words

    with open("datasets/dictionary_words.json", "w") as f:
        json.dump(words, f)

    print("  ✓ Generated: datasets/dictionary_words.json\n")

    # ========================================================================
    # Generate Test Cases
    # ========================================================================
    print("="*70)
    print("GENERATING TEST CASES")
    print("="*70 + "\n")

    test_cases = {
        "customer_ids": {
            "present": random.sample(customer_ids, 100),
            "absent": [1200000 + i for i in range(100)]  # IDs definitely not in dataset
        },
        "product_catalog": {
            "present": random.sample(product_ids, 100),
            "absent": [f"PROD{str(i).zfill(6)}" for i in range(60000, 60100)]
        },
        "config_settings": {
            "present": random.sample(config_keys, 50),
            "absent": [f"config.missing.{i:03d}" for i in range(50)]
        },
        "dictionary_words": {
            "present": random.sample(words, 100),
            "absent": [f"zzz_notfound_{i}" for i in range(100)]
        }
    }

    with open("datasets/test_cases.json", "w") as f:
        json.dump(test_cases, f, indent=2)

    print("✓ Test cases generated: datasets/test_cases.json")
    print("\nDataset generation complete!")
    print("\nYou can now implement your search algorithms in starter_code.py")
    print("and use these datasets to benchmark performance.\n")

if __name__ == "__main__":
    generate_datasets()