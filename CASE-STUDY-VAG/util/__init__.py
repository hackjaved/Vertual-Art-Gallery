import configparser
class PropertyUtil:
    @staticmethod
    def getPropertyString(property_file_path='C://Users//mubee//Downloads//case study-vag//case study-vag//util//PropertyFile.txt'):
        try:
            with open(property_file_path, 'r') as file:
                properties = {}
                for line in file:
                    key, value = line.strip().split('=')
                    properties[key.strip()] = value.strip()
                connection_string=f"DRIVER={{SQL Server}};" \
                                    f"SERVER={properties['hostname']};" \
                                    f"DATABASE={properties['dbname']};" \
                                    f"PORT={properties['port']};" \
                                    f"Trusted_Connection=yes;"
                return connection_string

        except ValueError as e:
            print("Dtabase is mising",e)

        except Exception as e:
            print(f"Error reading property file: {e}")
            return None