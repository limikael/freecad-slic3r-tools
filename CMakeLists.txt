
IF (BUILD_GUI)
    PYSIDE_WRAP_RC(Slcr_QRC_SRCS Resources/Slcr.qrc)
ENDIF (BUILD_GUI)

SET(Slcr_SRCS
    Init.py
    InitGui.py
    Slcr.py
    SlcrGui.py
)
SOURCE_GROUP("" FILES ${Slcr_SRCS})

ADD_CUSTOM_TARGET(Slcr ALL
    SOURCES ${Slcr_SRCS} ${Slcr_QRC_SRCS}
)

fc_copy_sources(Slcr "${CMAKE_BINARY_DIR}/Mod/Slcr" ${Slcr_SRCS})

IF (BUILD_GUI)
    fc_target_copy_resource(Slcr
        ${CMAKE_CURRENT_BINARY_DIR}
        ${CMAKE_BINARY_DIR}/Mod/Slcr
        Slcr_rc.py)
ENDIF (BUILD_GUI)

INSTALL(
    FILES
        ${Slcr_SRCS}
        ${Slcr_QRC_SRCS}
    DESTINATION
        Mod/Slcr
)

SET(SlcrGuiIcon_SVG
    Resources/icons/SlcrWorkbench.svg
)

fc_copy_sources(Slcr "${CMAKE_BINARY_DIR}/Mod/Slcr" ${SlcrGuiIcon_SVG})
INSTALL(FILES ${SlcrGuiIcon_SVG} DESTINATION "Mod/Slcr/Resources/icons")
