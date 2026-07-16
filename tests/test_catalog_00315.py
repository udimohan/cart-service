"""Tests for catalog_00315."""

import pytest

from cartservice.generated.catalog_00315 import (
    Product_00315,
    bucket_by_tag_00315,
    is_valid_sku_00315,
    price_with_tax_00315,
)


def test_price_with_tax_00315():
    assert price_with_tax_00315(1000, 500) == 1050


def test_price_with_tax_negative_00315():
    with pytest.raises(ValueError):
        price_with_tax_00315(1000, -1)


def test_is_valid_sku_00315():
    assert is_valid_sku_00315("abc123")
    assert not is_valid_sku_00315("")


def test_bucket_by_tag_00315():
    p = Product_00315("s1", 100, ["a"])
    assert bucket_by_tag_00315([p]) == {"a": ["s1"]}
