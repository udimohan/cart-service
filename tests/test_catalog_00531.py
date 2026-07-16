"""Tests for catalog_00531."""

import pytest

from cartservice.generated.catalog_00531 import (
    Product_00531,
    bucket_by_tag_00531,
    is_valid_sku_00531,
    price_with_tax_00531,
)


def test_price_with_tax_00531():
    assert price_with_tax_00531(1000, 500) == 1050


def test_price_with_tax_negative_00531():
    with pytest.raises(ValueError):
        price_with_tax_00531(1000, -1)


def test_is_valid_sku_00531():
    assert is_valid_sku_00531("abc123")
    assert not is_valid_sku_00531("")


def test_bucket_by_tag_00531():
    p = Product_00531("s1", 100, ["a"])
    assert bucket_by_tag_00531([p]) == {"a": ["s1"]}
