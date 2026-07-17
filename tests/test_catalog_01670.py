"""Tests for catalog_01670."""

import pytest

from cartservice.generated.catalog_01670 import (
    Product_01670,
    bucket_by_tag_01670,
    is_valid_sku_01670,
    price_with_tax_01670,
)


def test_price_with_tax_01670():
    assert price_with_tax_01670(1000, 500) == 1050


def test_price_with_tax_negative_01670():
    with pytest.raises(ValueError):
        price_with_tax_01670(1000, -1)


def test_is_valid_sku_01670():
    assert is_valid_sku_01670("abc123")
    assert not is_valid_sku_01670("")


def test_bucket_by_tag_01670():
    p = Product_01670("s1", 100, ["a"])
    assert bucket_by_tag_01670([p]) == {"a": ["s1"]}
