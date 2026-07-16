"""Tests for catalog_01276."""

import pytest

from cartservice.generated.catalog_01276 import (
    Product_01276,
    bucket_by_tag_01276,
    is_valid_sku_01276,
    price_with_tax_01276,
)


def test_price_with_tax_01276():
    assert price_with_tax_01276(1000, 500) == 1050


def test_price_with_tax_negative_01276():
    with pytest.raises(ValueError):
        price_with_tax_01276(1000, -1)


def test_is_valid_sku_01276():
    assert is_valid_sku_01276("abc123")
    assert not is_valid_sku_01276("")


def test_bucket_by_tag_01276():
    p = Product_01276("s1", 100, ["a"])
    assert bucket_by_tag_01276([p]) == {"a": ["s1"]}
