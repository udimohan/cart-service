"""Tests for catalog_00230."""

import pytest

from cartservice.generated.catalog_00230 import (
    Product_00230,
    bucket_by_tag_00230,
    is_valid_sku_00230,
    price_with_tax_00230,
)


def test_price_with_tax_00230():
    assert price_with_tax_00230(1000, 500) == 1050


def test_price_with_tax_negative_00230():
    with pytest.raises(ValueError):
        price_with_tax_00230(1000, -1)


def test_is_valid_sku_00230():
    assert is_valid_sku_00230("abc123")
    assert not is_valid_sku_00230("")


def test_bucket_by_tag_00230():
    p = Product_00230("s1", 100, ["a"])
    assert bucket_by_tag_00230([p]) == {"a": ["s1"]}
