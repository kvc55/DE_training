from log_setup import logger

TRANSPORTS = ['car', 'plane', 'ship', 'bicycle', 'bus']


def get_transport() -> str:
    """Takes index user's input and gives mean of transport from list.

    :return: mean of transport
    :rtype: str
    """

    try:
        index_transport = int(input('Enter an index: '))
        if index_transport >= 0:
            try:
                return TRANSPORTS[index_transport]
            except IndexError:
                logger.info('Index out of range.')
                return get_transport()
            except Exception as e:
                logger.info("Error occurred", e)
                return get_transport()
        else:
            logger.info("That's not a positive number.")
            return get_transport()
    except ValueError:
        logger.info("That's not an integer.")
        return get_transport()
    except Exception as e:
        logger.info("Error occurred", e)
        return get_transport()


if __name__ == "__main__":
    logger.info(f'Mean of transport: {get_transport()}')
