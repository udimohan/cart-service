"""Tests for catalog_00731."""

import pytest

from cartservice.generated.catalog_00731 import (
    Product_00731,
    bucket_by_tag_00731,
    is_valid_sku_00731,
    price_with_tax_00731,
)


def test_price_with_tax_00731():
    assert price_with_tax_00731(1000, 500) == 1050


def test_price_with_tax_negative_00731():
    with pytest.raises(ValueError):
        price_with_tax_00731(1000, -1)


def test_is_valid_sku_00731():
    assert is_valid_sku_00731("abc123")
    assert not is_valid_sku_00731("")


def test_bucket_by_tag_00731():
    p = Product_00731("s1", 100, ["a"])
    assert bucket_by_tag_00731([p]) == {"a": ["s1"]}
