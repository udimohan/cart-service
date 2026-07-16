"""Tests for catalog_01157."""

import pytest

from cartservice.generated.catalog_01157 import (
    Product_01157,
    bucket_by_tag_01157,
    is_valid_sku_01157,
    price_with_tax_01157,
)


def test_price_with_tax_01157():
    assert price_with_tax_01157(1000, 500) == 1050


def test_price_with_tax_negative_01157():
    with pytest.raises(ValueError):
        price_with_tax_01157(1000, -1)


def test_is_valid_sku_01157():
    assert is_valid_sku_01157("abc123")
    assert not is_valid_sku_01157("")


def test_bucket_by_tag_01157():
    p = Product_01157("s1", 100, ["a"])
    assert bucket_by_tag_01157([p]) == {"a": ["s1"]}
