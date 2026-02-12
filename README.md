# Assignment 3: Search Performance Analysis

## Setup Instructions

### 1. Clone this repository and open in VS Code

```bash
git clone <REPO_URL>
cd search-assignment
code .
```

### 2. Generate the test datasets

Run the data generator to create four datasets with different characteristics:

```bash
python data_generator.py
# You may need to run python3 data_generator.py
```

This will create:
- `datasets/customer_ids.json` - 100,000 unsorted customer IDs
- `datasets/product_catalog.json` - 50,000 pre-sorted product IDs
- `datasets/config_settings.json` - 500 small config keys (unsorted)
- `datasets/dictionary_words.json` - 10,000 sorted dictionary words
- `datasets/test_cases.json` - Test cases for validation

### 3. Implement your search algorithms

Open `starter_code.py` and complete the three search functions:
1. `linear_search()` - Sequential search through unsorted data
2. `binary_search_iterative()` - Iterative binary search on sorted data. **You that function is provided sorted data only**.
3. `binary_search_recursive()` - Recursive binary search on sorted data. **You that function is provided sorted data only**.

### 4. Test and benchmark

Uncomment the test functions in the `__main__` block:

```python
if __name__ == "__main__":
    test_search_correctness()        # Verify implementations work
    benchmark_all_datasets()         # Compare performance on all datasets
    analyze_preprocessing_costs()    # Analyze sorting trade-offs
```

Then run:

```bash
python starter_code.py
# or python3 starter_code.py
```

## The Four Scenarios

### Dataset A: Unsorted Customer IDs (100,000 entries)
**Scenario**: Customer service database where IDs arrive in order received  
**Question**: Is it worth sorting 100K entries to enable binary search?

### Dataset B: Pre-sorted Product Catalog (50,000 entries)
**Scenario**: E-commerce inventory system maintained in sorted order  
**Question**: How much faster is binary search on pre-sorted data?

### Dataset C: Small Config Settings (500 entries)
**Scenario**: Application configuration frequently accessed during runtime  
**Question**: Does algorithm choice matter for small datasets?

### Dataset D: Dictionary Words (10,000 entries)
**Scenario**: Autocomplete feature for search-as-you-type  
**Question**: Why keep dictionary sorted for prefix matching?

## What to Submit

Submit two files:
1. **Your completed Python file** (`starter_code.py` or rename to `search_analysis.py`)
2. **Written analysis document** (Google Doc or Word) containing:
   - Performance Results section (150-200 words)
   - Preprocessing Analysis section (150-200 words)
   - Algorithm Selection section (200-300 words)
   - Total: 500-700 words

Good luck! Remember: the best algorithm depends on your data characteristics and usage patterns.