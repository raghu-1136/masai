raw_tags = ["python", "data", "python", "ml", "data", "ai", "python", (1, 2), (1, 2), "ml"]

required_tags_1 = {"python", "data"}   # both present — should be a subset
required_tags_2 = {"python", "java"}   # "java" is absent — NOT a subset

def clean_tags(raw_tags):
    cleaned = set(raw_tags)
    print(f"Unique tag count: {len(cleaned)}")
    return cleaned

def check_required_subset(cleaned, required):
    name = "required_tags_1" if required == required_tags_1 else "required_tags_2"
    result = required.issubset(cleaned)
    print(f"{name} is a subset: {result}")
    return result

def make_frozen_hashable(cleaned):
    
    frozen = frozenset(cleaned)

    try:
        hash_value = hash(frozen)
        print(f"Frozen set hash: {hash_value}")
        return hash_value

    except TypeError as e:
        print(f"Hashing failed: {e}")
        return None

def demo_remove_vs_discard(cleaned, missing_tag):
    
    try: 
        cleaned.remove(missing_tag)
        
    except KeyError:
        print(f"KeyError: '{missing_tag}'is not in the  set")

    cleaned.discard(missing_tag)
    print(f"discard('{missing_tag}') completed without error")

cleaned = clean_tags(raw_tags)

check_required_subset(cleaned, required_tags_1)   
check_required_subset(cleaned, required_tags_2)

make_frozen_hashable(cleaned)

demo_remove_vs_discard(cleaned, "java")
