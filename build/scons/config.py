# MODE options are DEBUG, SIZE, PERFORMANCE, and RELEASE.

DEBUG_GCC = {
    #'CFLAGS': ['-Wstrict-prototypes'],
    'CCFLAGS': ['-Wall', '-g', '-fvisibility=hidden'],
}
DEBUG_MSVC = {
    'CCFLAGS': ['/nologo', '-W3'],
    'LINKFLAGS': ['/nologo'],
}

SIZE_GCC = {
    'CCFLAGS': ['-Wall', '-Os', '-flto', '-fvisibility=hidden'],
    'LINKFLAGS': ['-Os', '-flto'],
}
SIZE_MSVC = {
    'CCFLAGS': ['/nologo', '-W3', '-O1', '-GL', '-GS-'],
    'LINKFLAGS': ['/nologo', '-LTCG'],
}

PERFORMANCE_GCC = {
    'CCFLAGS': ['-Wall', '-O3', '-flto', '-fvisibility=hidden'],
    'LINKFLAGS': ['-O3', '-flto'],
}
PERFORMANCE_MSVC = {
    'CCFLAGS': ['/nologo', '-W3', '-O2', '-GL', '-GS-'],
    'LINKFLAGS': ['/nologo', '-LTCG'],
}

RELEASE_GCC = PERFORMANCE_GCC
RELEASE_MSVC = PERFORMANCE_MSVC
