from app.models.enums import ClusteringColorSpace


def test_clustering_color_space_members():
    # Test for existence of members
    assert ClusteringColorSpace.RGB, "RGB member should exist in ClusteringColorSpace"
    assert ClusteringColorSpace.HSL, "HSL member should exist in ClusteringColorSpace"
    assert ClusteringColorSpace.LAB, "LAB member should exist in ClusteringColorSpace"

def test_clustering_color_space_values():
    # Test for correctness of member values
    assert ClusteringColorSpace.RGB.value == "RGB", "RGB member should have value 'RGB'"
    assert ClusteringColorSpace.HSL.value == "HSL", "HSL member should have value 'HSL'"
    assert ClusteringColorSpace.LAB.value == "LAB", "LAB member should have value 'LAB'"

def test_clustering_color_space_iterable():
    # Optional: Test if enum is iterable and returns all members
    members = list(ClusteringColorSpace)
    assert len(members) == 3, "ClusteringColorSpace should have exactly 3 members"
    expected_members = ["RGB", "HSL", "LAB"]
    extracted_member_values = [member.value for member in members]
    assert all(value in extracted_member_values for value in expected_members), "All expected members should be in ClusteringColorSpace"
