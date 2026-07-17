"""Tests for catalog_00774."""

import pytest

from cartservice.generated.catalog_00774 import (
    Product_00774,
    bucket_by_tag_00774,
    is_valid_sku_00774,
    price_with_tax_00774,
)


def test_price_with_tax_00774():
    assert price_with_tax_00774(1000, 500) == 1050


def test_price_with_tax_negative_00774():
    with pytest.raises(ValueError):
        price_with_tax_00774(1000, -1)


def test_is_valid_sku_00774():
    assert is_valid_sku_00774("abc123")
    assert not is_valid_sku_00774("")


def test_bucket_by_tag_00774():
    p = Product_00774("s1", 100, ["a"])
    assert bucket_by_tag_00774([p]) == {"a": ["s1"]}
