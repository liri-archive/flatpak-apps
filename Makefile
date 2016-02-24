#all: org.hawaiios.systempreferences.app
all: org.hawaiios.terminal.app org.hawaiios.eyesight.app

%.app: %.json
	rm -rf app
	xdg-app-builder --ccache --require-changes --repo=repo --subject="Build of $<, `date`" ${EXPORT_ARGS} app $<
