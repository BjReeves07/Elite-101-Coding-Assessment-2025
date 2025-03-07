### Note: I feel that I do understand this program and would be able to do work like this in a job, but I often had to use documentation or other online resources to understand the python syntax, as I am much better in java so any ineffciency or something else is likely due to that.
def getFreeTables(tables):
    """Level 1: List all tables that are currently free."""
    return [table['table_id'] for table in tables if not table['occupied']]

def findOneTableForSize(tables, party_size):
    """Level 2: Find one table that can seat at least the party size and is free."""
    for table in tables:
        if not table['occupied'] and table['capacity'] >= party_size:
            return table['table_id']
    return None  # Return None if no suitable table is found

def findAllTablesForSize(tables, party_size):
    """Level 3: Return all tables that can seat the party size and are free."""
    return [table['table_id'] for table in tables if not table['occupied'] and table['capacity'] >= party_size]


def findTablesIncludingCombos(tables, party_size):
    """Level 4: Return all single or adjacent table combinations that can seat the party size."""
    suitable_tables = []
    # Check for single tables
    for table in tables:
        if not table['occupied'] and table['capacity'] >= party_size:
            suitable_tables.append([table['table_id']])
    # Check for combinations of adjacent tables
    for table in tables:
        if not table['occupied']:
            for neighbor_id in table['neighbors']:
                neighbor_table = next((t for t in tables if t['table_id'] == neighbor_id), None)
                if neighbor_table and not neighbor_table['occupied']:
                    combined_capacity = table['capacity'] + neighbor_table['capacity']
                    if combined_capacity >= party_size:
                        suitable_tables.append([table['table_id'], neighbor_table['table_id']])
    return suitable_tables
# -----------------------------------------------------------------------------
# Testing:
if __name__ == "__main__":
    tables_data = [
        {"table_id": 1, "capacity": 2, "occupied": False, "neighbors": [2]},
        {"table_id": 2, "capacity": 4, "occupied": True,  "neighbors": [1, 3]},
        {"table_id": 3, "capacity": 2, "occupied": False, "neighbors": [2, 4]},
        {"table_id": 4, "capacity": 6, "occupied": False, "neighbors": [3]}
    ]

    print("LEVEL 1: Free Tables =", getFreeTables(tables_data))

    print("LEVEL 2: One table for party size 2 =", findOneTableForSize(tables_data, 2))

    print("LEVEL 3: All tables for party size 2 =", findAllTablesForSize(tables_data, 2))

    combos = findTablesIncludingCombos(tables_data, 5)
    print("LEVEL 4: Single or combined tables for party size 5 =", combos)
