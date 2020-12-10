Version1 -- 

The python file ConvertUI.py is a python file that grabs a directory from a user, finds pdf files in that directory and
allows users to select pdf files to be converted to audio. Users can choose a start and end point to be coverted i.e.
they could convert only pages 13-26 to audio as this might be a chapter or important part of the pdf. The conversion is all
done behind a UI and at this stage it has not been tested, it works only with the right input and has no
exception handling.



dist and build --
Inside the dist folder there is an exe called ConverUI that has been made from the ConvertUI python file with the use of
pyinstaller. I believe that the ConertUI.spec file and the files in the build folder are the configuration for the exe file.

Upon testing this on my own system I encountered no errors, however when testing on another computer I recieved an AssertionError,
thorough testing was not conducted and I am not sure why such an error has occurred, this will be further investigated and any
updates will be added to a new version.
