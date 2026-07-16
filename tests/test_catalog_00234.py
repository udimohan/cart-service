"""Tests for catalog_00234."""

import pytest

from cartservice.generated.catalog_00234 import (
    Product_00234,
    bucket_by_tag_00234,
    is_valid_sku_00234,
    price_with_tax_00234,
)


def test_price_with_tax_00234():
    assert price_with_tax_00234(1000, 500) == 1050


def test_price_with_tax_negative_00234():
    with pytest.raises(ValueError):
        price_with_tax_00234(1000, -1)


def test_is_valid_sku_00234():
    assert is_valid_sku_00234("abc123")
    assert not is_valid_sku_00234("")


def test_bucket_by_tag_00234():
    p = Product_00234("s1", 100, ["a"])
    assert bucket_by_tag_00234([p]) == {"a": ["s1"]}
