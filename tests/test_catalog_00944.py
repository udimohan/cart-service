"""Tests for catalog_00944."""

import pytest

from cartservice.generated.catalog_00944 import (
    Product_00944,
    bucket_by_tag_00944,
    is_valid_sku_00944,
    price_with_tax_00944,
)


def test_price_with_tax_00944():
    assert price_with_tax_00944(1000, 500) == 1050


def test_price_with_tax_negative_00944():
    with pytest.raises(ValueError):
        price_with_tax_00944(1000, -1)


def test_is_valid_sku_00944():
    assert is_valid_sku_00944("abc123")
    assert not is_valid_sku_00944("")


def test_bucket_by_tag_00944():
    p = Product_00944("s1", 100, ["a"])
    assert bucket_by_tag_00944([p]) == {"a": ["s1"]}
