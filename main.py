import repository as informacio
import parse as parsejar_info

def main():
  informacio.obtenir_informacio_assignatures()
  parsejar_info.parse_per_aules()


main()
