from pylinac import Starshot

star_img = "D:\Git_Repo_personal\Medical_Physics\Gantry_starshot.tif"
mystar = Starshot(star_img, dpi=105, sid=1000)
mystar.analyze()
print(mystar.results())
mystar.plot_analyzed_image()