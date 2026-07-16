"""Tests for catalog_01531."""

import pytest

from cartservice.generated.catalog_01531 import (
    Product_01531,
    bucket_by_tag_01531,
    is_valid_sku_01531,
    price_with_tax_01531,
)


def test_price_with_tax_01531():
    assert price_with_tax_01531(1000, 500) == 1050


def test_price_with_tax_negative_01531():
    with pytest.raises(ValueError):
        price_with_tax_01531(1000, -1)


def test_is_valid_sku_01531():
    assert is_valid_sku_01531("abc123")
    assert not is_valid_sku_01531("")


def test_bucket_by_tag_01531():
    p = Product_01531("s1", 100, ["a"])
    assert bucket_by_tag_01531([p]) == {"a": ["s1"]}
