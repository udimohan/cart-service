"""Tests for catalog_01286."""

import pytest

from cartservice.generated.catalog_01286 import (
    Product_01286,
    bucket_by_tag_01286,
    is_valid_sku_01286,
    price_with_tax_01286,
)


def test_price_with_tax_01286():
    assert price_with_tax_01286(1000, 500) == 1050


def test_price_with_tax_negative_01286():
    with pytest.raises(ValueError):
        price_with_tax_01286(1000, -1)


def test_is_valid_sku_01286():
    assert is_valid_sku_01286("abc123")
    assert not is_valid_sku_01286("")


def test_bucket_by_tag_01286():
    p = Product_01286("s1", 100, ["a"])
    assert bucket_by_tag_01286([p]) == {"a": ["s1"]}
