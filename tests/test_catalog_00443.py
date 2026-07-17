"""Tests for catalog_00443."""

import pytest

from cartservice.generated.catalog_00443 import (
    Product_00443,
    bucket_by_tag_00443,
    is_valid_sku_00443,
    price_with_tax_00443,
)


def test_price_with_tax_00443():
    assert price_with_tax_00443(1000, 500) == 1050


def test_price_with_tax_negative_00443():
    with pytest.raises(ValueError):
        price_with_tax_00443(1000, -1)


def test_is_valid_sku_00443():
    assert is_valid_sku_00443("abc123")
    assert not is_valid_sku_00443("")


def test_bucket_by_tag_00443():
    p = Product_00443("s1", 100, ["a"])
    assert bucket_by_tag_00443([p]) == {"a": ["s1"]}
