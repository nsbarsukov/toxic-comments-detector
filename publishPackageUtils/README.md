
## Install package
```shell
pip install toxic-comments-detector
```

## Example
```python
from toxic-comments-detector import ToxicCommentsDetector

test_raw_texts = [
    'ты чего берега попутал?',
    'это правый берег реки, не путай с левым'
]

toxicDetector = ToxicCommentsDetector()
print(toxicDetector.predict(test_raw_texts))
```