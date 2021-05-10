
## Install package
```shell
pip install toxicity
```

## Example
```python
from toxicity import ToxicCommentsDetector

test_raw_texts = [
    'ты чего берега попутал?',
    'это правый берег реки, не путай с левым'
]

toxicDetector = ToxicCommentsDetector()
print(toxicDetector.predict(test_raw_texts))
```