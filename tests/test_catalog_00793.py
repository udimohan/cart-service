"""Tests for catalog_00793."""

import pytest

from cartservice.generated.catalog_00793 import (
    Product_00793,
    bucket_by_tag_00793,
    is_valid_sku_00793,
    price_with_tax_00793,
)


def test_price_with_tax_00793():
    assert price_with_tax_00793(1000, 500) == 1050


def test_price_with_tax_negative_00793():
    with pytest.raises(ValueError):
        price_with_tax_00793(1000, -1)


def test_is_valid_sku_00793():
    assert is_valid_sku_00793("abc123")
    assert not is_valid_sku_00793("")


def test_bucket_by_tag_00793():
    p = Product_00793("s1", 100, ["a"])
    assert bucket_by_tag_00793([p]) == {"a": ["s1"]}
