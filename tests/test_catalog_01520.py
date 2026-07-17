"""Tests for catalog_01520."""

import pytest

from cartservice.generated.catalog_01520 import (
    Product_01520,
    bucket_by_tag_01520,
    is_valid_sku_01520,
    price_with_tax_01520,
)


def test_price_with_tax_01520():
    assert price_with_tax_01520(1000, 500) == 1050


def test_price_with_tax_negative_01520():
    with pytest.raises(ValueError):
        price_with_tax_01520(1000, -1)


def test_is_valid_sku_01520():
    assert is_valid_sku_01520("abc123")
    assert not is_valid_sku_01520("")


def test_bucket_by_tag_01520():
    p = Product_01520("s1", 100, ["a"])
    assert bucket_by_tag_01520([p]) == {"a": ["s1"]}
