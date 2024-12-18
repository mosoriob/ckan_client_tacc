from ckan_client_tacc.models.ckan.responses.member_response import (
    Member,
    MemberResponse,
)


def test_member_response():
    # Sample response data matching the actual API response
    response_data = {
        "help": "https://ckan.tacc.utexas.edu/api/3/action/help_show?name=member_list",
        "success": True,
        "result": [
            ["e1e3625e-1139-442a-8210-6ab070bafad2", "user", "Admin"],
            ["7003d3c9-8596-45b4-9064-7194bd09b187", "user", "Member"],
        ],
    }

    # Create MemberResponse instance
    member_response = MemberResponse(**response_data)

    # Assert the values are correctly set
    assert member_response.help == response_data["help"]
    assert member_response.success == response_data["success"]
    assert len(member_response.result) == 2

    member_first = Member(member_response.result[0])
    # Test first member (Admin)
    assert member_first.id == "e1e3625e-1139-442a-8210-6ab070bafad2"
    assert member_first.type == "user"
    assert member_first.role == "Admin"

    member_second = Member(member_response.result[1])
    assert member_second.id == "7003d3c9-8596-45b4-9064-7194bd09b187"
    assert member_second.type == "user"
    assert member_second.role == "Member"
