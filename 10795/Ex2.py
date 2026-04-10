print("Insira uma nota: ")
nota = int(input())

match nota:
    
    case n if nota >= 90:
        print("Excelente")
    case n if nota >= 70 and nota <= 89:
        print("Bom")
    case n if nota >= 50 and nota <= 69:
        print("Suficiente")
    case n if nota <= 49:
        print("Insuficiente")




#Link de onde consegui a informação do "n if nota"
#https://www.google.com/search?q=can+i+write+a+%22%3C%22+in+a+match+case&sca_esv=f6dab0cbe71090ff&biw=1920&bih=911&sxsrf=ANbL-n4kAxHDnReP7wYrwmKPp7keYdcBFw%3A1775825596154&ei=vPLYaf2RCZnV7M8PnPCy2AE&ved=0ahUKEwj9393uqeOTAxWZKvsDHRy4DBsQ4dUDCBE&uact=5&oq=can+i+write+a+%22%3C%22+in+a+match+case&gs_lp=Egxnd3Mtd2l6LXNlcnAiIWNhbiBpIHdyaXRlIGEgIjwiIGluIGEgbWF0Y2ggY2FzZTIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABSKY4UABY1zdwAXgBkAEAmAFpoAHBFKoBBDMyLjG4AQPIAQD4AQGYAiKgAqoVwgIKEAAYgAQYigUYQ8ICCxAAGIAEGLEDGIMBwgIEEAAYA8ICDhAAGIAEGIoFGLEDGIMBwgIOEC4YgAQYigUYsQMYgwHCAgoQLhiABBiKBRhDwgILEC4YgAQYsQMYgwHCAgQQLhgDwgIREC4YgAQYsQMYgwEYxwEY0QPCAgUQLhiABMICCBAuGIAEGLEDwgIFEAAYgATCAgsQLhiABBjHARivAcICIBAuGIAEGLEDGIMBGMcBGNEDGJcFGNwEGN4EGOAE2AEBwgIIEAAYFhgeGArCAgYQABgWGB7CAgUQABjvBcICBRAhGJ8FmAMAugYGCAEQARgUkgcEMzEuM6AHwfgBsgcEMzAuM7gHpxXCBwYyLjI3LjXIB0qACAE&sclient=gws-wiz-serp