import sys, os, subprocess

if len(sys.argv)!=2:
	print("Wrong parameters.")
else:
	rootdir = sys.argv[1]
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			print("Importing " + file)
			print("mvn install:install-file -Dfile=" + os.path.join(subdir, file) + " -DgroupId=" + file.rstrip(".jar") + " -DartifactId=" + file.rstrip(".jar") + " -Dversion=1.0" + " -Dpackaging=jar" + " -DgeneratePom=true")
			subprocess.run(["mvn", "install:install-file", "-Dfile=" + os.path.join(subdir, file), "-DgroupId=" + file.rstrip(".jar"), "-DartifactId=" + file.rstrip(".jar"), "-Dversion=1.0", "-Dpackaging=jar", "-DgeneratePom=true"], shell=True)			
			with open('dependencies.txt', 'a') as output:
				output.write("<dependency>\n")
				output.write("\t<groupId>" + file.rstrip(".jar") + "</groupId>\n")
				output.write("\t<artifactId>" + file.rstrip(".jar") + "</artifactId>\n")
				output.write("\t<version>1.0</version>\n")
				output.write("</dependency>\n\n")
	  
	print("Process terminated successfully.")
