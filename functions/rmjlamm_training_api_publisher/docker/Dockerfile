# using easikit base python image
FROM 151571714362.dkr.ecr.eu-west-2.amazonaws.com/easikit/easikit-python-base:latest

# change this string if you want to rebuild your docker image after
# changes to easiutils or other core dependency, doesn't matter what to
RUN REBUILD_STRING=poptarts

# copy the library files (which will change a bits)
# (but are pre-requisits for requirements.txt)
COPY target/common_module common_module
RUN cd common_module; python -m build; cd -

# copy and install python modules (which will rarely change)
COPY target/requirements.txt .
RUN pip3 install -r requirements.txt --disable-pip-version-check

# copy the function.properties and application files (which will change constantly)
COPY target/handler/ handler
COPY target/function.properties .

CMD [ "app.handler" ]
