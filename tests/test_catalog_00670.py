"""Tests for catalog_00670."""

import pytest

from cartservice.generated.catalog_00670 import (
    Product_00670,
    bucket_by_tag_00670,
    is_valid_sku_00670,
    price_with_tax_00670,
)


def test_price_with_tax_00670():
    assert price_with_tax_00670(1000, 500) == 1050


def test_price_with_tax_negative_00670():
    with pytest.raises(ValueError):
        price_with_tax_00670(1000, -1)


def test_is_valid_sku_00670():
    assert is_valid_sku_00670("abc123")
    assert not is_valid_sku_00670("")


def test_bucket_by_tag_00670():
    p = Product_00670("s1", 100, ["a"])
    assert bucket_by_tag_00670([p]) == {"a": ["s1"]}
