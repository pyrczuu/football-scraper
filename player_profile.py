def save_if_absent(connection, logger, path: str):
    player_id = "" #TODO extract from url

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM players WHERE id = (%d);"
        cursor.execute(query, player_id)
        rows = cursor.fetchall()

        if len(rows) == 0:
            pass # TODO post player data

        cursor.close()

    except Exception as error:
        logger.info(f"Error fetching data: {error}")