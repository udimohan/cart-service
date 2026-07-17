"""Tests for catalog_01055."""

import pytest

from cartservice.generated.catalog_01055 import (
    Product_01055,
    bucket_by_tag_01055,
    is_valid_sku_01055,
    price_with_tax_01055,
)


def test_price_with_tax_01055():
    assert price_with_tax_01055(1000, 500) == 1050


def test_price_with_tax_negative_01055():
    with pytest.raises(ValueError):
        price_with_tax_01055(1000, -1)


def test_is_valid_sku_01055():
    assert is_valid_sku_01055("abc123")
    assert not is_valid_sku_01055("")


def test_bucket_by_tag_01055():
    p = Product_01055("s1", 100, ["a"])
    assert bucket_by_tag_01055([p]) == {"a": ["s1"]}
