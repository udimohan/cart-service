"""Tests for catalog_01002."""

import pytest

from cartservice.generated.catalog_01002 import (
    Product_01002,
    bucket_by_tag_01002,
    is_valid_sku_01002,
    price_with_tax_01002,
)


def test_price_with_tax_01002():
    assert price_with_tax_01002(1000, 500) == 1050


def test_price_with_tax_negative_01002():
    with pytest.raises(ValueError):
        price_with_tax_01002(1000, -1)


def test_is_valid_sku_01002():
    assert is_valid_sku_01002("abc123")
    assert not is_valid_sku_01002("")


def test_bucket_by_tag_01002():
    p = Product_01002("s1", 100, ["a"])
    assert bucket_by_tag_01002([p]) == {"a": ["s1"]}
