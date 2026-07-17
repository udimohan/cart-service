"""Tests for catalog_01680."""

import pytest

from cartservice.generated.catalog_01680 import (
    Product_01680,
    bucket_by_tag_01680,
    is_valid_sku_01680,
    price_with_tax_01680,
)


def test_price_with_tax_01680():
    assert price_with_tax_01680(1000, 500) == 1050


def test_price_with_tax_negative_01680():
    with pytest.raises(ValueError):
        price_with_tax_01680(1000, -1)


def test_is_valid_sku_01680():
    assert is_valid_sku_01680("abc123")
    assert not is_valid_sku_01680("")


def test_bucket_by_tag_01680():
    p = Product_01680("s1", 100, ["a"])
    assert bucket_by_tag_01680([p]) == {"a": ["s1"]}
