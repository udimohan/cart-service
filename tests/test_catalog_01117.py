"""Tests for catalog_01117."""

import pytest

from cartservice.generated.catalog_01117 import (
    Product_01117,
    bucket_by_tag_01117,
    is_valid_sku_01117,
    price_with_tax_01117,
)


def test_price_with_tax_01117():
    assert price_with_tax_01117(1000, 500) == 1050


def test_price_with_tax_negative_01117():
    with pytest.raises(ValueError):
        price_with_tax_01117(1000, -1)


def test_is_valid_sku_01117():
    assert is_valid_sku_01117("abc123")
    assert not is_valid_sku_01117("")


def test_bucket_by_tag_01117():
    p = Product_01117("s1", 100, ["a"])
    assert bucket_by_tag_01117([p]) == {"a": ["s1"]}
