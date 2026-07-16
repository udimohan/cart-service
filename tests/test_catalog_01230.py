"""Tests for catalog_01230."""

import pytest

from cartservice.generated.catalog_01230 import (
    Product_01230,
    bucket_by_tag_01230,
    is_valid_sku_01230,
    price_with_tax_01230,
)


def test_price_with_tax_01230():
    assert price_with_tax_01230(1000, 500) == 1050


def test_price_with_tax_negative_01230():
    with pytest.raises(ValueError):
        price_with_tax_01230(1000, -1)


def test_is_valid_sku_01230():
    assert is_valid_sku_01230("abc123")
    assert not is_valid_sku_01230("")


def test_bucket_by_tag_01230():
    p = Product_01230("s1", 100, ["a"])
    assert bucket_by_tag_01230([p]) == {"a": ["s1"]}
