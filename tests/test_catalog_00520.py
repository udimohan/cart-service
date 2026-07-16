"""Tests for catalog_00520."""

import pytest

from cartservice.generated.catalog_00520 import (
    Product_00520,
    bucket_by_tag_00520,
    is_valid_sku_00520,
    price_with_tax_00520,
)


def test_price_with_tax_00520():
    assert price_with_tax_00520(1000, 500) == 1050


def test_price_with_tax_negative_00520():
    with pytest.raises(ValueError):
        price_with_tax_00520(1000, -1)


def test_is_valid_sku_00520():
    assert is_valid_sku_00520("abc123")
    assert not is_valid_sku_00520("")


def test_bucket_by_tag_00520():
    p = Product_00520("s1", 100, ["a"])
    assert bucket_by_tag_00520([p]) == {"a": ["s1"]}
