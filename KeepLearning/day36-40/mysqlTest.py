import pymysql
import openpyxl


def insert_fun(conn):
    """插入函数"""
    # no = int(input("部门编号："))
    # name = input("部门名称：")
    # location = input("部门所在地:")

    info = [
        ["50", "组织部", "南京"],
        ["60", "纪检部", "安徽"],
        ["70", "统战部", "洛阳"],
        ["80", "办公室", "太原"],
    ]
    try:
        with conn.cursor() as cursor:
            # affected_rows = cursor.execute(
            #     "insert into `tb_dept` values(%s,%s,%s)",
            #     (no, name, loaction),
            # )
            affected_rows = cursor.executemany(
                "insert into `tb_dept` values(%s,%s,%s)", info
            )
            if affected_rows == len(info):  # affected_rows==1
                print("新增部门成功！")
            else:
                print("部分新增成功！")
        conn.commit()
    except pymysql.MySQLError as err:
        conn.rollback()
        print(type(err), err)
    finally:
        conn.close()


def delete_fun(conn):
    """删除函数"""
    no = int(input("部门编号："))
    try:
        with conn.cursor() as cursor:
            affected_rows = cursor.execute(
                "delete from `tb_dept` where `dno`=%s", (no,)
            )
            if affected_rows == 1:
                print("删除部门成功!!!")
    except pymysql.MySQLError as err:
        conn.rollback()
        print(type(err), err)
    finally:
        conn.close()


def update_fun(conn):
    """更新函数"""
    no = int(input("部门编号: "))
    name = input("部门名称: ")
    location = input("部门所在地: ")

    try:
        with conn.cursor() as cursor:
            affected_rows = cursor.execute(
                "update `tb_dept` set `dname`=%s,`dloc`=%s where `dno`=%s",
                (name, location, no),
            )
        if affected_rows == 1:
            print("更新部门信息成功!")
        conn.commit()
    except pymysql.MySQLError as err:
        conn.rollback()
        print(type(err), err)
    finally:
        conn.close()


def select_fun(conn):
    """查询函数"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("select `dno`,`dname`,`dloc` from `tb_dept`")
            row = cursor.fetchone()
            # 如何使用iter函数构造一个迭代器
            # 来逐行抓取数据
            while row:
                print(row)
                row = cursor.fetchone()
    except pymysql.MySQLError as err:
        print(type(err), err)
    finally:
        conn.close()


def emp_select(conn):
    """分页查询员工数据"""
    page = int(input("页码: "))
    size = int(input("大小: "))
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "select `eno`,`ename`,`job`,`sal` from `tb_emp` order by `sal` desc limit %s,%s",
                ((page - 1) * size, size),
            )
            for emp_dict in cursor.fetchall():
                print(emp_dict)
    except pymysql.MySQLError as err:
        print(type(err), err)
    finally:
        conn.close()


def sql_to_exl(conn):
    """将MySQL数据库数据导出Excel"""
    # 怎么把exl文件导入mysql？
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "员工基本信息"
    sheet.append(("工号", "姓名", "职位", "月薪", "补贴", "部门"))
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "select `eno`,`ename`,`job`,`sal`,coalesce(`comm`,0),`dname` from `tb_emp` natural join `tb_dept`"
            )
            row = cursor.fetchone()
            while row:
                sheet.append(row)
                row = cursor.fetchone()
        workbook.save("./hrs.xlsx")
        print("保存完成")
    except pymysql.MySQLError as err:
        print(err)
    finally:
        # 关闭连接释放资源
        conn.close()


def excel_to_mysql(conn):
    """将excel文件导入数据库表中"""
    # 读取excel文件，逐行调用insert_fun()


def main():
    """主函数"""
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="guest",
        password="Guest.618",
        database="hrs",
        charset="utf8mb4",
        # autocommit=True,
    )
    # insert_fun(conn)
    # delete_fun(conn)
    # update_fun(conn)
    # select_fun(conn)
    # emp_select(conn)
    sql_to_exl(conn)


if __name__ == "__main__":
    main()
